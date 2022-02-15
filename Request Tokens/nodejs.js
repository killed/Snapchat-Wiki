"use strict";

// Libraries
const { createHash } = require("crypto");

// Variables
var hashPattern = "0001110111101110001111010101111011010001001110011000110001000110";
var secret = "iEk21fuwZApXlz93750dmW22pw389dPwOk";

function requestToken(token, timestamp) {
    var firstHash = createHash("sha256").update(secret + token, "binary").digest("hex");
    var secondHash = createHash("sha256").update(timestamp + secret, "binary").digest("hex");

    var result = "";

    for (var i = 0; i < hashPattern.length; i++)
        if (hashPattern[i] == "0")
            result += firstHash[i];
        else
            result += secondHash[i];

    return result;
}

console.log(requestToken("m198sOkJEn37DjqZ32lpRu76xmw288xSQ9", Date.now()));