// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Types {

    uint public num;

    // Assign value
    function setValue(uint _num) public {
        num = _num;
    }

    // If-Else condition check
    function checkValue() public view returns (string memory) {
        if (num > 10) {
            return "Greater";
        } else {
            return "Not Greater";
        }
    }
}