/// <reference path="jquery.d.ts" />

module Templates{
	export class Template{
		_workspace: Workspace.Workspace;
		_templateCache: JQuery;
		constructor(workspace: Workspace.Workspace){
			this._workspace = workspace;
		}

		initialize(url: string){
			// load templates
			var self = this;
			return($.get("/html/templates.htm",
				function(data){
					self._templateCache = $(data);
				}
			));
		}
	}
}