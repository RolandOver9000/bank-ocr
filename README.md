# bank-ocr coding test

This is the link of the description of the test: https://codingdojo.org/kata/BankOCR/  
I have got a 5th user story, that says handle hexadecimal digits.

How you can use my solution?
  - Pull the repository.
  - If you want to add new bank codes, (or just overwrite my dummy codes) put them into dummy_data.txt . 
    - Each bank code has 4 rows.
    - Each digit of the code takes 3 columns and 3 rows thus it is 9 character long.
  - If you want to run my code:
    - Install Python's 3.6.9 version or above.
    - Open command line and navigate it to my project's root path.
    - Chose which user story you want to check:
      - User story 1 - switch to feature/convert-data branch - command: **git checkout feature/convert-data**
      - User story 2 - switch to feature/account-number-validation branch - command: **git checkout feature/account-number-validation**
      - User story 3 - switch to feature/handle-wrong-code branch - command: **git checkout feature/handle-wrong-code branch**
      - User story 4 - switch to feature/fix-wrong-code branch - command: **git checkout feature/fix-wrong-code**
      - User story 5 - switch to feature/switch-to-hexadecimal branch - command: **git checkout feature/switch-to-hexadecimal**
     - I made the tests on develop/test branch - command: **git checkout develop/test**
     - To run my code type **python3 main.py** in the command line.
     - You will see a result on each branch on your command line.
     - From User story 3 you will see a result file in /bank-ocr/data/validated_dummy_data.txt.
  - Tests are available only on develop/test, development, master branches.
  - If you want to check the test results:
    - Navigate your command line to my project's root path.
    - Type **python3 -m unittest discover -v**.
