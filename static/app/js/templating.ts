/// <reference path="jquery.d.ts" />

module Templates{
	export class Templates{
		_workspace: Workspace.Workspace;
		_templateCache: JQuery;
		constructor(workspace: Workspace.Workspace){
			this._workspace = workspace;

			// load templates
			var templatesHtml: string = "";
			$.get("html/templates.htm",
				function(data){
					alert(data);
				}
			);
		}
	}
}