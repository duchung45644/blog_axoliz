import { goto } from '$app/navigation';

export function isAuthenticated() {
	return !!localStorage.getItem('token');
}

export function requireAuth() {
	if (!isAuthenticated()) {
		goto('/login'); // Chuyển hướng nếu chưa đăng nhập
	}
}
