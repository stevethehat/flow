/// <reference path="jquery.d.ts" />
/// <reference path="handlebars.d.ts" />

module Templates{
	export class Templates{
		_workspace: Workspace.Workspace;
		_templateCache: JQuery;
		_templates: any;

		constructor(workspace: Workspace.Workspace){
			var self: Templates = this;
			this._workspace = workspace;
			this._templates = {};

			Handlebars.registerHelper('iconPath', 
				function(icon) {
					/*
					return(
						new Handlebars.SafeString(self._workspace.iconPath + '/32x32/' + icon + '.png');
					);
					*/
					return(self._workspace.iconPath + '/32x32/' + icon + '.png');
				}	
			);
		}

		render(id: string, data: any, result: any){
			var self: Templates = this;
			var html: string = '';
			var template: any;

			if(this._templates[id]){
				template = this._templates[id];
				result(template(data));
			} else {var template: any;
				$.get('/html/templates/' + id + '.htm',
					function(templateCode){
						template = Handlebars.compile(templateCode);
						self._templates[id] = template;
						result(template(data));
					}
				);
			}
		}
	}
}