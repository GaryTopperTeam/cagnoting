import logging

from keycloak import KeycloakOpenID


LOG = logging.getLogger(__name__)


class Auth(KeycloakOpenID):

    def __init__(self, server_url, client_id, realm_name):
        KeycloakOpenID.__init__(self,
                                server_url=server_url,
                                client_id=client_id,
                                realm_name=realm_name)

        self.audience = client_id
        self._public_key = '\n'.join(["-----BEGIN PUBLIC KEY-----",
                                      KeycloakOpenID.public_key(self),
                                      "-----END PUBLIC KEY-----"])
        self.token_algo = self.certs()['keys'][0]['alg']

    def public_key(self):
        return self._public_key
