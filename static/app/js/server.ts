/// <reference path="libdef/jquery.d.ts" />
/// <reference path="menus.ts" />

module Flow.Server {
	'use strict';

	export class Server {
		private host: string;
		private baseUrl: string;

		constructor(host: string, baseUrl: string) {
			this.host = host;
			this.baseUrl = baseUrl;
		}

		get(uid: string, action: string, data: any, callback: any): void{
			var url: string = '/' + this.baseUrl + '/' + uid + '/' + action;
			var ajaxParameters = {
				url: url,
				success: function (data: any) {
					callback(data);
				},
				error: function (request: any, textStatus: string, errorThrown: string) {
					alert('Error (' + url + ') ' + request.responseText + ' ' + textStatus + ' ' + errorThrown);
				}
			};
			$.ajax(ajaxParameters);
		}
	}
}
