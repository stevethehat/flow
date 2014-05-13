/// <reference path="jquery.d.ts" />

module Listings{
    export interface ListItem {
        uid: string;
        description: string;
        icon?: string;
    }

    export interface ListItems {
        [index: number]: ListItem;
    }

    export interface List{
    	parentUid: string;
    	items: ListItems;
    }

	export class ListView{
		_workspace: Workspace.Workspace;
		_container: JQuery;
		constructor(workspace: Workspace.Workspace, container: JQuery){
			this._workspace = workspace;
			this._container = container;
		}

		populate(list: List){
			this._container.empty();
			var ul: JQuery = $('<ul/>').addClass('list-group').appendTo(this._container);
			for(var id in list.items){
				var item: ListItem = list.items[id];
				var li: JQuery = $('<li/>')
					.addClass('list-group-item')
					.appendTo(ul);
				var icon: JQuery = $('<img/>')
					.attr('src', '/assets/icons/32x32/book_spelling.png')
					.appendTo(li);
				var description: JQuery = $('<span/>')
					.text(item.description)
					.appendTo(li);
			}
		}
	}
}