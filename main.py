#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import webapp2
import constants
from appengine_config import DEBUG
from webapp2 import Route as route
from google.appengine.ext import ereporter, ndb
import handler
import model

ereporter.register_logger()

logging.getLogger().setLevel(logging.DEBUG)


class Subscribe(handler.Base):
  def post(self):
    email = self.request.get('email')
    if email:
      e = model.Email(key=ndb.Key(model.Email, email))
      e.put()
      self.session['subscription'] = email
    return self.redirect('/')


main_routes = [
  route(r'/api/remains/<currency:[A-Z]+>', 'remains.RemainsAPIHandler'),
  route(r'/people', 'handler.Static', defaults={'template': 'people.html'}),
  route(r'/business', 'handler.Static', defaults={'template': 'business.html'}),
  route(r'/investors', 'handler.Static', defaults={'template': 'investors.html'}),
  route(r'/developers', 'handler.Static', defaults={'template': 'developers.html'}),
  route(r'/press', 'handler.Static', defaults={'template': 'press.html'}),
  route(r'/', 'handler.Static', 'home', defaults={'template': 'index.html'}),
  route(r'/login', 'handler.Static', defaults={'template': 'login.html'}),
  route(r'/team', 'handler.Static', defaults={'template': 'team.html'}),
  route(r'/invest', 'handler.Static', defaults={'template': 'invest.html'}),
  route(r'/wiki', 'handler.Static', defaults={'template': 'wiki.html'}),
  route(r'/wallet', 'handler.Static', defaults={'template': 'wallet.html'}),

  route(r'/pie', 'handler.Static', defaults={'template': 'pie.html'}),
  route(r'/explorer', 'handler.Static', defaults={'template': 'explorer.html'}),
  route(r'/subscribe', Subscribe),

  route(r'/about', 'handler.Static', defaults={'template': 'about.html'}),
  route(r'/supply', 'handler.Static', defaults={'template': 'supply.html'}),

  route('/deposit', 'deposit.Deposit'),
  route('/deposit/blockchain/callback', 'deposit.BlockchainCallback'),

  route('/admin', 'admin.Admin'),
  route('/admin/assets', 'admin.AssetsHandler'),
  route('/admin/operations', 'admin.OperationsHandler'),
  route('/admin/transactions', 'admin.TxsHandler'),
  route('/admin/transactions/put', 'admin.TxPutHandler'),
  route('/admin/transactions/rollback', 'admin.TxRollbackHandler'),
  route('/admin/transactions/process', 'admin.TxProcessHandler'),
  route('/admin/transactions/import', 'admin.TxImportHandler'),
  route('/admin/transactions/index', 'admin.TxIndexHandler'),
  route('/admin/transactions/flush', 'admin.TxFlushHandler'),
  route('/admin/transactions/json/accounts', 'admin.Json:accounts'),
  route('/admin/transactions/json/assets', 'admin.Json:assets'),
  route('/admin/transactions/json/tags', 'admin.Json:tags'),
  route('/admin/transactions/json/unapplied', 'admin.Json:unapplied'),
  route('/admin/transactions/json/pie', 'admin.Json:pie'),
  route('/admin/accounts', 'admin.PubKeysHandler'),
  route('/admin/accounts/put', 'admin.PubKeysHandler'),
  route('/admin/accounts/import', 'admin.PubKeysImportHandler'),

  route('/profile', 'auth.Profile', 'profile'),
  route('/logout', 'auth.SignOut', 'logout'),
  route('/login/google', 'auth.Google', 'login-google'),
  route('/login/google/callback', 'auth.Google:callback', 'login-google-callback'),
  route('/login/facebook', 'auth.Facebook', 'login-facebook'),
  route('/login/facebook/callback', 'auth.Facebook:callback', 'login-facebook-callback'),
  route('/login/github', 'auth.Github', 'login-github'),
  route('/login/github/callback', 'auth.Github:callback', 'login-github-callback'),
  route('/login/vk', 'auth.Vk', 'login-vk'),
  route('/login/vk/callback', 'auth.Vk:callback', 'login-vk-callback'),
  route('/login/twitter', 'auth.Twitter', 'login-twitter'),
  route('/login/twitter/callback', 'auth.Twitter:callback', 'login-twitter-callback'),
  route('/login/angellist', 'auth.AngelList', 'login-angel'),
  route('/login/angellist/callback', 'auth.AngelList:callback', 'login-angel-callback'),
]

application = webapp2.WSGIApplication(main_routes, debug=DEBUG, config=constants.WEBAPP2_CONFIG)
