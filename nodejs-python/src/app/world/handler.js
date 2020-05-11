"use strict";

const uuid = require("uuid/v4");

module.exports.world = async () => {
  return {
    headers: {
      "Content-Type": "application/json",
    },
    statusCode: 200,
    body: JSON.stringify({ message: `olá nodejs 1111 ${uuid()}` }),
  };
};
