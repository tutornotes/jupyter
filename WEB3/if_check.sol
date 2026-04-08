// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Types {

    uint public num;

    // Assign value to state variable
    function setValue(uint _num) public {
        num = _num;
    }

    // Check condition using if statement
    function checkValue() public view returns (string memory) {
        if (num > 10) {
            return "Greater";
        }
        return "Smaller";
    }
}