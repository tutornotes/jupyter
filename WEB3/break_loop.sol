// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Types {

    uint[] public arr;

    // Function using while loop with break
    function fillArray() public {
        delete arr; // reset array
        uint i = 1;

        while (true) {
            arr.push(i);

            if (i == 5) {
                break; // terminate loop when condition met
            }

            i++;
        }
    }

    // Return array elements
    function getArray() public view returns (uint[] memory) {
        return arr;
    }
}