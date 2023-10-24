#!/usr/bin/node
// Computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    const userIdCompletion = {};
    json.forEach(todo => {
      if (todo.completed) {
        if (userIdCompletion[todo.userId] !== undefined) {
          userIdCompletion[todo.userId] += 1;
        } else userIdCompletion[todo.userId] = 1;
      }
    });

    console.log(userIdCompletion);
  }
});
