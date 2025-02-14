<!-- src/lib/components/Input.svelte -->
<script>
	export let type = 'text';
	export let placeholder = '';
	export let value = '';
</script>

<input {type} bind:value {placeholder} class="rounded border px-4 py-2" />
