// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Types {

    uint[] public arr;

    // Initialize array using while loop
    function fillArray() public {
        delete arr; // reset array
        uint i = 1;

        while (i <= 5) {
            arr.push(i);
            i++;
        }
    }

    // Return array elements
    function getArray() public view returns (uint[] memory) {
        return arr;
    }
}