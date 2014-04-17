/// <reference path="jquery.d.ts" />
var Menus;
(function (Menus) {
    var MainMenu = (function () {
        function MainMenu() {
        }
        MainMenu.prototype.populate = function (elements) {
            return ("hello");
        };
        return MainMenu;
    })();
    Menus.MainMenu = MainMenu;
})(Menus || (Menus = {}));
/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
var Workspace;
(function (_Workspace) {
    var Workspace = (function () {
        function Workspace() {
            var mainMenu = new Menus.MainMenu();
            mainMenu.populate([
                { label: 'menu item1' },
                { label: 'hgjgjghjgjgj', icon: 'hello' },
                { label: 'sadadssa' }
            ]);
        }
        Workspace.prototype.test = function () {
            return ("hello");
        };
        return Workspace;
    })();
})(Workspace || (Workspace = {}));
