#!/usr/bin/node

const request = require('request');
const argument = process.argv;

request(argument[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // console.log(JSON.parse(body))
    let taskCompleted = 0;
    const myJson = JSON.parse(body);
    const myDict = {};
    for (let i = 0; i < myJson.length; i++) {
      try {
        if (i === myJson.length - 1) {
          myDict[myJson[i].userId] = taskCompleted;
        } else if (myJson[i - 1].userId !== myJson[i].userId) {
          myDict[myJson[i - 1].userId] = taskCompleted;
          taskCompleted = 0;
        }
      } catch (error) {

      } finally {
        if (myJson[i].completed === true) {
          taskCompleted += 1;
        }
      }
    }

    console.log(myDict);
  }
});
