"use strict";

const uuid = require("uuid/v4");

module.exports.world = async () => {
  return {
    headers: {
      "Content-Type": "text/plan",
    },
    statusCode: 200,
    body: `olá nodejs ${uuid()}`,
  };
};
