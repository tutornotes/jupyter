// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Types {

    uint[] public arr;

    // Simulated do-while loop
    function initializeArray() public {
        delete arr; // reset array
        uint i = 1;

        while (true) {
            arr.push(i);

            i++;

            if (i > 5) {
                break; // ensures loop runs at least once
            }
        }
    }

    // Return array values
    function getArray() public view returns (uint[] memory) {
        return arr;
    }
}