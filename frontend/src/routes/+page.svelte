<script>
    import { goto } from '$app/navigation';
    import { user } from '../stores/auth';
    import { Pane, Splitpanes } from 'svelte-splitpanes';
    import { onMount } from 'svelte';
    import { Input, Label, Helper, Button, P} from 'flowbite-svelte';

    onMount(() => {
    });

    let responseVal = "";
    let chatVal = [];
    let totalEmissions = 0.0;

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
            totalEmissions += data["emissions"];
          });
    }

</script>
  
<main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Chat</h1>
    <p class="text-gray-500">Sup dawgzzzz</p>
    <Splitpanes class="default-theme" style="height: 400px">
      <Pane>
		<Splitpanes class="default-theme" horizontal="{true}">
			<Pane minSize={70} class="pane" >
        <div style= "max-height:250px; overflow-y:auto ">
          {#each chatVal as chat, index}
            <div style="padding-left:20px; padding-right:20px;" >
              
                {#if index % 2 == 0}
                  <P align="right" color="text-blue-700 dark:text-blue-500" size="xl">{chat}</P>
                {:else}
                  <P align="left" size="xl">{chat}</P>
                {/if}
            </div>
          {/each} 
        </div>       
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
      <Pane>
        <div>
          <P align="center" size="4xl" weight="extrabold">Carbon Dioxide Emissions:</P>
          <P align="center" size="4xl" weight="extrabold">{totalEmissions}</P>
        </div>
      </Pane>
    </Splitpanes>
  </main>

  <style>
    .pane {
      height: 200px; /* Set a fixed height */
      overflow-y: auto; /* Add vertical scrolling */
    }
  </style>
  
