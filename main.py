#!/usr/bin/env python
# Hairpiar Korean 2012 Chrome Games Rank Server.
# @ragingwind

import os
import webapp2
import logging
import datetime
import random
from django.utils import simplejson as json

from google.appengine.ext import db
from google.appengine.api import users


class Ranker(db.Model):
	game_name = db.StringProperty(required=True)
	user_name = db.StringProperty(required=True)
	recorded = db.DateProperty()
	score = db.IntegerProperty()
	
	@staticmethod
	def rank(game_name, score):
		q = db.Query(Ranker)
		q.filter('game_name', game_name)
		q.filter('score >', score)
		logging.info('RANK' + str(q.count()) + ' ' + str(score))
		return q.count() == 0 and 1 or q.count() + 1

class UserHandler(webapp2.RequestHandler):
	def get(self, user_name):
		self.response.out.write(user_name)

	def post(self):
		data = json.loads(self.request.POST['ranker'])
		q = Ranker.gql('WHERE game_name=:1 and user_name=:2', data['game_name'], data['user_name'])
		
		ranker = ''

		if q.count() > 0:
			ranker = q.get()
			ranker.score = int(data['score'])
			ranker.put()
		else:
			ranker = Ranker(key_name=data['user_name'], game_name=data['game_name'], 
				user_name=data['user_name'], score=int(data['score']), 
				recorded=datetime.datetime.now().date())
		
		rank = Ranker.rank(ranker.game_name, ranker.score)
		ranker.put()
		
		res = {'game_name':ranker.game_name, 'user_name':ranker.user_name, 
			'score':ranker.score, 'rank':rank}
		logging.info(json.dumps(res))
		self.response.out.write(json.dumps(res))

class TopRankHandler(webapp2.RequestHandler):
	def get(self, game_name, limit):
		logging.info(game_name + ' ' + str(limit))
		q = db.Query(Ranker)
		q.filter('game_name', game_name)
		q.order('-score')
		rankers = q.fetch(int(limit))
		res = []
		for r in rankers:
			user = {'game_name':r.game_name, 'user_name':r.user_name, 
			'score':r.score}
			res.append(user)
		logging.info(json.dumps(res))
		self.response.out.write(json.dumps(res))


class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

app = webapp2.WSGIApplication([
	webapp2.Route('/', MainHandler),
	webapp2.Route('/top/<game_name>/<limit>', TopRankHandler),
	webapp2.Route('/user/', UserHandler),
	webapp2.Route('/user/<user_name>', UserHandler),
], debug=True)
