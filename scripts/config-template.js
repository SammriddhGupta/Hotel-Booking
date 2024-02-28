const config = {
    cognito: {
        identityPoolId: "REPLACE_WITH_YOUR_IDENTITY_POOL_ID",
        cognitoDomain: "REPLACE_WITH_YOUR_COGNITO_DOMAIN",
        appId: "REPLACE_WITH_YOUR_APP_ID",
    },
};

var cognitoApp = {
    auth: {},
    Init: function () {
      var authData = {
        ClientId: config.cognito.appId,
        AppWebDomain: config.cognito.cognitoDomain,
        TokenScopesArray: ["email", "openid", "profile"],
        RedirectUriSignIn: "http://localhost:8080/hotel/",
        RedirectUriSignOut: "http://localhost:8080/hotel/",
        UserPoolId: config.cognito.identityPoolId,
        AdvancedSecurityDataCollectionFlag: false,
        Storage: null,
      };
  
      cognitoApp.auth = new AmazonCognitoIdentity.CognitoAuth(authData);
      cognitoApp.auth.userhandler = {
        onSuccess: function (result) {},
        onFailure: function (err) {},
      };
    },
  };