import pymongo

class MongoCon:

    def __connect(self):
        connection = pymongo.MongoClient('localhost', 27017)
        db = connection.medicalTerm
        return db.terminalogy

    def update_word(self, words):
        collection = self.__connect()

        for word in words:
            collection.update_one({'_id': word['word']}, {'$push': {'mean': word['mean'], 'ref': word['ref']}}
                                  , upsert=True)
