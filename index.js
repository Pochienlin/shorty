// API constants
const headers = {
    "Content-Type": "text/json",
    "Access-Control-Allow-Origin": "*"
};
//      API endpoint
var api_endpoint_url = `http://127.0.0.1:5000/add`

// Vue app start, mount as #app: 
const app = Vue.createApp({
    data(){
        return {
            shortweb: "",
            longweb: "http://",
            logo: 'default.gif',
            status: "COPY"
        } //end of return
    },
    methods: {
        // on submission click, shakes the longweb input bar, calls dockered API to retrieve shortened URL and display using moustache notated div
        post_url(){
            this.status="COPY"
            // console.log("sending: ", {"new_url":`${this.longweb}`})
            // http://localhost:5000/add?new_url=https://www.amazon.com
            axios.post(`${api_endpoint_url}?new_url=${this.longweb}`,{
                headers:headers,
                body:JSON.stringify({
                "new_url":this.longweb
                })
            })
            .then(response => {
                // console.log("new url logged: ",this.longweb)
                // Inspect the response
                // console.log('======= post url axios executed=========')
                // console.log(response)
                //      store response data in Vue model
                this.shortweb = response.data
                // console.log('======= post url axios ended=========')
                // this.logo = "confirmation.gif"
            })
            .catch(error => {
                console.log(error.message)
            })
        },
        
        // when submission button is pressed, copies shortened URL into clipboard
        copy_to_board(){          
            
            /* Copy the text inside the text field */
            navigator.clipboard.writeText(this.shortweb);
          
            /* flash the copied text */
            this.status="COPIED!"
          }
      
    },

    computed:{
    }
})

app.mount('#app')
//          retrieve COUNT and figure out what the new URL will be
//          set this new path end as a variable "new_path"
var new_path=""
//          set this new path end's to be that of vue's data object (so that it displays when user inserts url)

// function that calls the api to add_new() with route "127.0.0.1:5000/add" with POST
function add_URL(input){
    //API call
    //retrieve response
    return true
}
