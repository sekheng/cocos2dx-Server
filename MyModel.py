from google.appengine.ext import ndb

class HighScore(ndb.Model):
	mScore = ndb.FloatProperty()
	mName =  ndb.StringProperty()
	isDeleted = ndb.BooleanProperty()
	@staticmethod
	def CreateHighscore(_score, _name):
		return HighScore(mScore = _score, mName = _name, isDeleted = False)