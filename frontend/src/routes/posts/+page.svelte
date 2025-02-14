<!-- src/routes/Posts.svelte -->
<script lang="ts">
	import { onMount } from 'svelte';
	import { getPosts } from '$lib/api';

	type Post = {
		title: string;
		content: string;
	};

	let posts: Post[] = [];

	onMount(async () => {
		posts = await getPosts();
	});
</script>

<div class="mx-auto max-w-lg p-4">
	<h2 class="mb-4 text-2xl font-bold">Danh sách bài viết</h2>
	{#each posts as post}
		<div class="mb-2 rounded border p-4">
			<h3 class="text-lg font-semibold">{post.title}</h3>
			<p>{post.content}</p>
		</div>
	{/each}
</div>
