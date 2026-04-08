// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Solidity_var_Test {

    function getSum() public pure returns (uint) {
        uint a = 10;   // local variable
        uint b = 20;   // local variable

        uint sum = a + b;
        return sum;
    }
}