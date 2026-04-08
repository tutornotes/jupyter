// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SolidityTest {

    uint a = 20;
    uint b = 5;

    function add() public pure returns (uint) {
        uint x = 20;
        uint y = 5;
        return x + y;
    }

    function subtract() public pure returns (uint) {
        uint x = 20;
        uint y = 5;
        return x - y;
    }

    function multiply() public pure returns (uint) {
        uint x = 20;
        uint y = 5;
        return x * y;
    }

    function divide() public pure returns (uint) {
        uint x = 20;
        uint y = 5;
        return x / y;
    }

    function modulus() public pure returns (uint) {
        uint x = 20;
        uint y = 5;
        return x % y;
    }
}