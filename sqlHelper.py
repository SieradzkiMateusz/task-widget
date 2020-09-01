import logging
from PySide2.QtCore import Qt, Slot, QDir, QFile
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel

table_name = "Tasks"


def createTable():
    if table_name in QSqlDatabase.database().tables():
        return

    query = QSqlQuery()
    if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS 'Tasks' (
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'title' TEXT NOT NULL,
                'status' INTEGER NOT NULL
                )
                """
            ):
        logging.error("Failed to query database")

    logging.info(query)


class SqlTaskModel(QSqlTableModel):
    def __init__(self, parent=None):
        super(SqlTaskModel, self).__init__(parent)

        createTable()
        self.setTable(table_name)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.select()
        logging.debug("Table was loaded successfully.")

    def insert(self, data):
        new_record = self.record()
        new_record.setValue("title", data['title'])
        new_record.setValue("status", 0)

        if not self.insertRecord(self.rowCount(), new_record):
            logging.error("Failed to insert data.")

        self.submitAll()
        self.select()

    def getTask(self):
        q = QSqlQuery("SELECT * FROM Tasks WHERE status is 0 LIMIT 1")
        q.first()
        rec = q.record()

        titleCol = rec.indexOf("title")
        idCol = rec.indexOf("id")

        return q.value(idCol), q.value(titleCol)

    def updateTaskStatus(self, taskID):
        query = QSqlQuery()
        query.prepare("UPDATE Tasks SET status=1 WHERE id=:id")
        query.bindValue(':id', taskID)
        query.exec_()

logging.basicConfig(filename='tasks.log', level=logging.DEBUG)
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

    filename = "{}/tasks-database.sqlite3".format(write_dir.absolutePath())

    database.setDatabaseName(filename)
    if not database.open():
        logger.error("Cannot open database")
        QFile.remove(filename)

if __name__ == "__main__":
    connectToDatabase()
    sql_task_model = SqlTaskModel()

