<script>

import http from '@/utils/http'

function addCagnoting (value) {
  return http.post('/api/cagnoting/', {value})
}

function getCagnoting () {
  return http.get('/api/cagnoting/')
}

export default {
    addCagnoting,
    getCagnoting,
};

</script>