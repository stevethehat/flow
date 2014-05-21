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
    	iconPath?: string;
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
			var self: ListView = this;
			this._container.empty();
			list.iconPath = self._workspace.iconPath;
			this._workspace.template.render('list', list,
				function(html){
					self._container.html(html);

					self._container.find('li').click(
						function(event){
							event.stopPropagation();

							var li: JQuery = $(event.target);
							var uid: string = li.attr('data-flowuid');

							self._container.find('li').removeClass('selected');

							li.addClass('selected');
							selectEvent(uid, li);
						}
					);

					self._container.find('li span.list-nav').click(
						function(event){
							event.stopPropagation();

							var li: JQuery = $(event.target).parent();
							var uid: string = li.attr('data-flowuid');

							self._container.find('li').removeClass('selected');

							li.addClass('selected');
							navigateEvent(uid, li);
						}
					);					
				}
			);
		}
	}
}