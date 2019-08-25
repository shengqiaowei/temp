*** Settings ***
Library  pylib/WebOpAdmin.py

Suite Setup  run keywords  open_browser1
...          AND  login  auto  sdfsdfsdf

Suite Teardown    close_browser1