Feature: ToolsQa | TextBox

    Scenario Outline: User registers successfully.
        Given I am at the Text Box Page "https://demoqa.com/text-box"
        And I add Full Name "<fullname>"
        And I add Email "<email>"
        And I add Current Address "<current_address>"
        And I add Permanent Address "<permanent_address>" 
        When I click on the Submit button
        Then I <should or should not> see a log message with the information submited in the form

    Examples:
        | fullname | email            | current_address      | permanent_address     | should or should not |
        | Zulema   | zulema@gmail.com | xxx xxxx, xxx, usa   | xxx xxxx, xxx, mex    | should               |
        | blabla   | blablaa@gmail.com| xxx xxxx, xxx, bla   | xxx xxxx, xxx, bla    | should               |
        | Iveth    | ivethgmail.com   | xxx xxxx, xxx, usa   | xxx xxxx, xxx, mex     | should not           |
