// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Test {

    // Function to calculate square of a number
    function sqrt(uint _num) public pure returns (uint) {
        return _num * _num;
    }

    // Function calling another function
    function add() public pure returns (uint) {
        uint value = 5;

        uint result = sqrt(value); // function call

        return result + 10; // final result
    }
}