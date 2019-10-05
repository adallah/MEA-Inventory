export const getHeader = function(data) {
    if(data !== undefined && data !==  'undefined'){
      var token = JSON.parse(data)
      const headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization' : token.token_type + ' ' + token.access_token
      }
      return headers
    }
  }