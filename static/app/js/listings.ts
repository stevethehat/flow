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

    export interface ListSelect{
    	(uid: string, listItem: JQuery): void;
    }

    export interface ListNavigate{
    	(uid: string, listItem:JQuery): void;
    }

	export class ListView{
		_workspace: Workspace.Workspace;
		_container: JQuery;
		constructor(workspace: Workspace.Workspace, container: JQuery){
			this._workspace = workspace;
			this._container = container;
		}

		populate(list: List, selectEvent?: ListSelect, navigateEvent?: ListNavigate){
			this._container.empty();
			var ul:JQuery = $('<ul/>').addClass('list-group').appendTo(this._container);
			for(var id in list.items){
				var item: ListItem = list.items[id];
				var li: JQuery = $('<li/>')
					.addClass('list-group-item')
					.appendTo(ul);

				if(selectEvent !== null){
					li.click(
						function(event){
							event.stopPropagation();
							ul.find('li').removeClass('selected');
							li.addClass('selected');
							selectEvent(item.uid, li);
						}
					);
				}

				var iconUrl: string = item.icon;
				if(icon !== null){
					iconUrl = this._workspace.iconPath + '/32x32/' + item.icon + '.png'
				} else {
					iconUrl = this._workspace.iconPath + '/32x32/book_spelling.png'
				}

				var icon: JQuery = $('<img/>')
					.attr('src', iconUrl)
					.appendTo(li);

				var description: JQuery = $('<span/>')
					.text(item.description)
					.appendTo(li);

				var navigate: JQuery = $('<span/>')
					.addClass('pull-right list-nav')
					.appendTo(li);

				if(navigateEvent !== null){
					navigate.click(
						function(event){
							event.stopPropagation();
							navigateEvent(item.uid, li);
						}
					);
				}

				var navigateIcon: JQuery = $('<i/>').
					addClass('fa fa-chevron-circle-right fa-lg pull-right')
					.appendTo(navigate);
			}
		}
	}
}