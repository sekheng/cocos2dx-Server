from google.appengine.ext import ndb

class HighScore:
	mScore = ndb.FloatProperty()
	mName =  ndb.StringProperty()
	
	@staticmethod
	def CreateHighscore(_score, _name):
		return HighScore(mScore = _score, mName = _name)