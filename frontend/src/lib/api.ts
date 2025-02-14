import axios from 'axios';

import { auth } from '$lib/store';

const API_BASE = 'http://localhost:8000'; // Thay đổi theo backend của bạn

// Tạo instance axios
const api = axios.create({
	baseURL: API_BASE,
	headers: { 'Content-Type': 'application/json' }
});

// Thêm token vào header nếu có
// Hàm cập nhật token từ store
export function setAuthToken() {
	auth.subscribe((state) => {
		if (state.token) {
			api.defaults.headers.common['Authorization'] = `Bearer ${state.token}`;
		} else {
			delete api.defaults.headers.common['Authorization'];
		}
	});
}

// Hàm gọi API chung
export async function apiRequest(method: string, url: string, data: any = null) {
	try {
		const response = await api({
			method,
			url,
			data
		});
		return response.data;
	} catch (error: any) {
		console.error('API Error:', error.response?.data || error.message);
		throw error;
	}
}

// Các hàm cụ thể
export const login = (username: any, password: any) =>
	apiRequest('post', '/login', { username, password });
export const getPosts = () => apiRequest('get', '/posts');
export const createPost = (post: any) => apiRequest('post', '/posts', post);
export const getUsers = () => apiRequest('get', '/users');
