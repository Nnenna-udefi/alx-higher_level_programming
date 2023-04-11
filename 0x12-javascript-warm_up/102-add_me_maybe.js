#!/usr/bin/node

/*
 * Inside the function, we first increment the counter for the given number
 * by setting this[number] to (this[number] || 0) + 1.
 * The || 0 part handles the case where this[number] is undefined,
 * which happens the first time we call the function with a particular number
 */

exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  this[number] = (this[number] || 0) + 1;
  return theFunction();
};
