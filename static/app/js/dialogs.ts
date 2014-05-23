module Flow.Dialogs {
	'use strict';

	export interface IButton {
		label: string;
	}
	export interface IButtons {
		[index: number]: IButton;
	}
}
