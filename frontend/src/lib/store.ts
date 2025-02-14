// src/lib/store.js
import { writable } from 'svelte/store';
import { login } from './api';

export const auth = writable({
	user: null,
	token: null
});

// Hàm đăng nhập
export async function handleLogin(username: any, password: any) {
	try {
		const data = await login(username, password);
		auth.set({ user: username, token: data.access_token });
		return data;
	} catch (error) {
		console.error('Login failed:', error);
	}
}

// Hàm đăng xuất
export function handleLogout() {
	auth.set({ user: null, token: null });
}

export function setAuthToken(apiInstance: {
	defaults: { headers: { common: { [x: string]: any } } };
}) {
	auth.subscribe((state) => {
		if (state.token) {
			apiInstance.defaults.headers.common['Authorization'] = `Bearer ${state.token}`;
		} else {
			delete apiInstance.defaults.headers.common['Authorization'];
		}
	});
}
