# Test Cases – Simulated Device Monitoring and Alert System

**Name:** Villanueva, Uan Gabriel D. 

**Student Number:*** 2601415

**Section:** 1CPE-B

**Date Tested:** November 3, 2026

Initial data for every test: `[28, 31, 35, 37, 29]`. Each test starts a fresh run of the program.

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Showed Reading 1 to Reading 5: 28, 31, 35, 37, 29 °C | Pass |
| TC02 | Choose 2, enter 33 | "Reading added successfully." | Showed "Reading added successfully."; choosing 1 afterwards listed 6 readings, the last being 33 °C | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Showed "Invalid input. Enter a whole number only."; choosing 1 still listed the original 5 readings | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100."; list still had 5 readings | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100."; list still had 5 readings | Pass |
| TC06 | Choose 2, add 30, then choose 3 | 30 °C -> WARNING | 30 was added, then option 3 showed "30 °C -> WARNING" | Pass |
| TC07 | Choose 3 (initial data) | 35 °C -> WARNING | Showed "35 °C -> WARNING" (also 28 NORMAL, 31 WARNING, 37 CRITICAL, 29 NORMAL) | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Showed Total 160, Average 32.00 °C, Min 28 °C, Max 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), Overall Status: ATTENTION REQUIRED | Pass |
| TC09 | Enter 9 at the menu | Error message; menu shown again | Showed "Invalid choice. Please enter a number from 1 to 5." and displayed the menu again | Pass |
| TC10 | Choose 5 | Exit message; program ends | Showed "Thank you for using the Device Monitoring System." and the program ended | Pass |
| TC11 | Choose 2, press Enter only (empty) | Rejected; list unchanged | Showed "Invalid input. The reading cannot be empty."; list still had 5 readings | Pass |
| TC12 | Choose 2, enter 3.5 | Rejected; list unchanged | Showed "Invalid input. Enter a whole number only."; list still had 5 readings | Pass |
| TC13 | Choose 2, enter 0; choose 2, enter 100 | Both accepted (range boundaries) | Both showed "Reading added successfully."; list ended with 0 °C and 100 °C as readings 6 and 7 | Pass |
| TC14 | Choose 2, enter 101 | Rejected; list unchanged | Showed "Invalid reading. Enter a value from 0 to 100."; list still had 5 readings | Pass |
| TC15 | Choose 2, enter 33, then choose 4 | Summary updates: 6 readings, total 193, avg 32.17, status ATTENTION REQUIRED | Showed Number 6, Total 193, Average 32.17 °C, Min 28, Max 37, NORMAL 2 (33.33%), WARNING 3 (50.00%), CRITICAL 1 (16.67%), ATTENTION REQUIRED | Pass |

**Result: 15 tests performed, 15 passed, 0 failed.**

## Bugs Found and Fixed

- No test failed when I ran the program, so I did not have a bug to fix. The hardest tests to get right were TC06 and TC07, the 30 °C and 35 °C boundaries. The rule says 30 to 35 °C inclusive is WARNING, so the upper limit needs `<=` and not `<`. In `classify_reading()` I used `elif reading <= critical_limit`, so 35 stays WARNING and only values above 35 become CRITICAL. I also confirmed that 30 is not NORMAL, because the NORMAL check is `reading < warning_limit` (strictly below 30).
