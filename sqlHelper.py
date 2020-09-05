import logging
from PySide2.QtCore import Qt, Slot, QDir, QFile
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel

# Table names for convenience
task_table = "tasks"
category_table = "category" 


def createTaskTable():
    # Don't create if table already exists
    if task_table in QSqlDatabase.database().tables():
        return

    query = QSqlQuery()
    if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS 'tasks' (
                'task_id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'cat_id' INTEGER,
                'title' TEXT NOT NULL,
                'status' INTEGER,
                FOREIGN KEY('cat_id') REFERENCES categories('category_id')
                )
                """
            ):
        logging.error("Failed to create task table")

    logging.info(query)

def createCategoryTable():
    # Don't create if table already exists
    if category_table in QSqlDatabase.database().tables():
        return

    query = QSqlQuery()
    if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS 'categories' (
                'category_id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'title' TEXT NOT NULL,
                'color' TEXT NOT NULL
                )
                """
            ):
        logging.error("Failed to create categories table")

class SqlTaskModel(QSqlTableModel):
    def __init__(self, parent=None):
        super(SqlTaskModel, self).__init__(parent)

        createTaskTable()
        self.setTable(task_table)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.select()
        # logging.debug("Task table was loaded successfully.")

    def insert(self, data):
        # Add new record to the table
        new_record = self.record()
        new_record.setValue("title", data['title'])
        new_record.setValue("status", 0)

        if not self.insertRecord(self.rowCount(), new_record):
            logging.error("Failed to insert data into tasks table.")

        self.submitAll()
        self.select()

    def getTask(self):
        # Get the first uncompleted task
        q = QSqlQuery("SELECT * FROM tasks WHERE status is 0 LIMIT 1")
        q.first()
        rec = q.record()

        titleCol = rec.indexOf("title")
        idCol = rec.indexOf("task_id")

        return q.value(idCol), q.value(titleCol)

    def updateTaskStatus(self, taskID):
        # Set task status as completed
        query = QSqlQuery()
        query.prepare("UPDATE tasks SET status=1 WHERE task_id=:id")
        query.bindValue(':id', taskID)
        query.exec_()


class SqlCategoryModel(QSqlTableModel):
    def __init__(self, parent=None):
        super(SqlCategoryModel, self).__init__(parent)

        createCategoryTable()
        self.setTable(category_table)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.select()
        # logging.debug("Category table loaded successfully.")
        
    def insert(self, data):
        # Add new record to the table
        new_record = self.record()
        new_record.setValue("title", data['title'])
        new_record.setValue("color", data['color'])

        if not self.insertRecord(self.rowCount(), new_record):
            logging.error("Failed to insert data into category table.")

        self.submitAll()
        self.select()

    def getCategories(self):
        # Get all categories from database
        q = QSqlQuery("SELECT * FROM categories")
        categories = []
        while (q.next()):
            rec = q.record()
            idCol = rec.indexOf("category_id")
            titleCol = rec.indexOf("title")
            colorCol = rec.indexOf("color")

            category = {
                    'catID': q.value(idCol),
                    'title': q.value(titleCol),
                    'color': q.value(colorCol)
            }
            categories.append(category)

        return categories
        
logging.basicConfig(filename='sqlite.log', level=logging.DEBUG)
logger = logging.getLogger("logger")

def connectToDatabase():
    database = QSqlDatabase.database()
    if not database.isValid():
        database = QSqlDatabase.addDatabase("QSQLITE")
        if not database.isValid():
            logger.error("Cannot add database")

    write_dir = QDir()
    if not write_dir.mkpath("."):
        logger.error("Failed to create writable directory")

    filename = "{}/app-database.sqlite3".format(write_dir.absolutePath())

    database.setDatabaseName(filename)
    if not database.open():
        logger.error("Cannot open database")
        QFile.remove(filename)

