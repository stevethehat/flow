/// <reference path="jquery.d.ts" />
/// <reference path="actions.ts" />
var Menus;
(function (Menus) {
    var BarMenu = (function () {
        function BarMenu(workspace, container) {
            this._workspace = workspace;
            this._container = container;
            this._container.attr('role', 'navigation').addClass('navbar navbar-default');

            this._containerFluid = this._container.append('div').addClass('container-fluid');

            this._containerFluid.append("button").attr('type', 'button');
        }
        BarMenu.prototype.populate = function (elements) {
            alert('populate' + elements);
        };

        BarMenu.prototype.addElement = function () {
        };
        return BarMenu;
    })();
    Menus.BarMenu = BarMenu;
})(Menus || (Menus = {}));
/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
var Server;
(function (_Server) {
    var Server = (function () {
        function Server(host, baseUrl) {
            this._host = host;
            this._baseUrl = baseUrl;
        }
        Server.prototype.get = function (uid, action, data, callback) {
            var url = '/' + this._baseUrl + '/' + uid + '/' + action;
            var ajaxParameters = {
                url: url,
                success: function (data) {
                    callback(data);
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    alert('Error (' + url + ') ' + XMLHttpRequest.responseText + ' ' + textStatus + ' ' + errorThrown);
                }
            };
            $.ajax(ajaxParameters);
        };
        return Server;
    })();
    _Server.Server = Server;
})(Server || (Server = {}));
/// <reference path="jquery.d.ts" />
/// <reference path="menus.ts" />
/// <reference path="server.ts" />
var Workspace;
(function (_Workspace) {
    var Workspace = (function () {
        function Workspace() {
            this.iconPath = '/assets/icons';
            this.body = $('body');
            this.header = $('#header');
            this.contentArea = $('#listing1');
            if (typeof window.innerWidth != 'undefined') {
                this.width = window.innerWidth, this.height = window.innerHeight;
            }
            this.contentArea.height(this.height - this.header.height() - 60);
            this.listview = new Listings.ListView(this, this.contentArea);

            this.server = new Server.Server("localhost", "html");
            this.server.get("1", "workspacemenu", null, function (data) {
                //mainMenu.populate(<Actions.ActionElements>data);
            });

            this.navigate('1');
        }
        Workspace.prototype.log = function () {
            alert('in log');
        };
        Workspace.prototype.navigate = function (uid) {
            this.listview.populate({
                parentUid: '1',
                items: [
                    { description: 'hello1', uid: '2', icon: 'beer' },
                    { description: 'hello2', uid: '3', icon: 'bell' }
                ]
            }, function (uid, item) {
                alert('select');
                this.listview.setSelected(item);
                alert('after call');
            }, function () {
                alert('navigate');
            });
        };
        Workspace.prototype.runAction = function () {
        };
        return Workspace;
    })();
    _Workspace.Workspace = Workspace;

    $(document).ready(function () {
        var workspace = new Workspace();
    });
})(Workspace || (Workspace = {}));
/// <reference path="jquery.d.ts" />
var Listings;
(function (Listings) {
    var ListView = (function () {
        function ListView(workspace, container) {
            this._workspace = workspace;
            this._container = container;
        }
        ListView.prototype.populate = function (list, selectEvent, navigateEvent) {
            this._container.empty();
            var ul = $('<ul/>').addClass('list-group').appendTo(this._container);
            for (var id in list.items) {
                var item = list.items[id];
                var li = $('<li/>').addClass('list-group-item').appendTo(ul);

                if (selectEvent !== null) {
                    li.click(function (event) {
                        event.stopPropagation();
                        ul.find('li').removeClass('selected');
                        li.addClass('selected');
                        selectEvent(item.uid, li);
                    });
                }

                var iconUrl = item.icon;
                if (icon !== null) {
                    iconUrl = this._workspace.iconPath + '/32x32/' + item.icon + '.png';
                } else {
                    iconUrl = this._workspace.iconPath + '/32x32/book_spelling.png';
                }

                var icon = $('<img/>').attr('src', iconUrl).appendTo(li);

                var description = $('<span/>').text(item.description).appendTo(li);

                var navigate = $('<span/>').addClass('pull-right list-nav').appendTo(li);

                if (navigateEvent !== null) {
                    navigate.click(function (event) {
                        event.stopPropagation();
                        navigateEvent(item.uid, li);
                    });
                }

                var navigateIcon = $('<i/>').addClass('fa fa-chevron-circle-right fa-lg pull-right').appendTo(navigate);
            }
        };
        return ListView;
    })();
    Listings.ListView = ListView;
})(Listings || (Listings = {}));
