const express = require('express');
const router = express.Router();
const usersApiController = require('../../controller/api/usersApi');

router.get('/', usersApiController.index);

router.post('/login', usersApiController.login);

router.post('/signup', usersApiController.signup);

module.exports = router;