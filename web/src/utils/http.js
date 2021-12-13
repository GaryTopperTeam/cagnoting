import axios from 'axios'

const http = axios.create({
  // baseURL: 'http://127.0.0.1:9019/',
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 50000,
  // headers: {
  //   Authorization: 'Bearer ' + window.localStorage.getItem('jwtToken')
  // }
})

http.interceptors.request.use(config => {
  return config
}, error => {
  // Do something with request error
  console.log('Error in config interceptors: ') // for debug
  console.log(error) // for debug
  Promise.reject(error)
})

http.interceptors.response.use(
  response => {
    const res = response
    if (res.status < 200 || res.status > 299) {
      return Promise.reject(new Error('error'))
    } else {
      if ('content-disposition' in response.headers &&
      response.headers['content-disposition'].includes('attachment')) {
        return response
      }
      return response.data
    }
  },
  error => {
    if (error.response.status === 403) {
      if (typeof error.response.data === 'string' ||
          error.response.data instanceof String) {
        if (error.response.data.includes('User not logged or no token received')) {
          window.location.reload()
        }
      } else if ('message' in error.response.data) {
        if (error.response.data.message === 'User not logged or no token received') {
          window.location.reload()
        }
      }
    }
    /* Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    }) */
    return Promise.reject(error)
  },
)

export default http
