/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />

module Workspace{
    class Workspace {
        constructor() {
            MainMenu mainMenu = new MainMenu();
        }
        body: JQuery;
        test() {
            return ("hello");
        }
    }
}