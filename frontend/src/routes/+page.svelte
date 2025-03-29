<script>
    import { goto } from '$app/navigation';
    import { user } from '../stores/auth';
    import { Pane, Splitpanes } from 'svelte-splitpanes';
    import { onMount } from 'svelte';
    import { Input, Label, Helper, Button} from 'flowbite-svelte';

    onMount(() => {
    });

    let responseVal = "";
    let chatVal = [];

    function handleClick(){
      chatVal = [...chatVal, responseVal];
      addResponse(responseVal);
      responseVal = "";
    }

    
    function addResponse(response_message) {
        fetch('http://localhost:8000/chat/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: response_message
            })
        })
        .then((response) => response.json())
        .then((data) => {
            // getResponse();
            chatVal = [...chatVal, data["chat_response"]];
          });
    }

</script>
  
<main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Chat</h1>
    <p class="text-gray-500">Sup dawgzzzz</p>
    <Splitpanes class="default-theme" style="height: 400px">
      <Pane>
		<Splitpanes class="default-theme" horizontal="{true}">
			<Pane minSize={70} >
        {#each chatVal as chat}
          <div>
            {chat}
          </div>
        {/each}
      </Pane>
			<Pane>
        <div class="mb-6">
          <Label for="Query" class="mb-2">Talk to the chat bot</Label>
          <Input type="text" id="response" placeholder="Type here..." bind:value={responseVal} >
            <Button type="submit" on:click={() => handleClick()} slot="right">Send</Button>
        </Input>
        </div>
      </Pane>
		</Splitpanes>
    </Pane>
      <Pane>This is where environmental info will go</Pane>
    </Splitpanes>
  </main>
  
  