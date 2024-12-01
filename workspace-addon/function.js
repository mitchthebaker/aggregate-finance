/**
 * Cloud Function that loads the homepage for a
 * Google Workspace Add-on.
 *
 * @param {Object} req Request sent from Google
 * @param {Object} res Response to send back
 */
exports.loadHomePage = function addonsHomePage (req, res) {
  res.send(createAction());
};

/** Creates a card with two widgets. */
function createAction() {
  return {
    "action": {
      "navigations": [
        {
          "pushCard": {
            "header": {
              "title": "Cats!"
            },
            "sections": [
              {
                "widgets": [
                  {
                    "textParagraph": {
                      "text": "Your random cat:"
                    }
                  },
                  {
                    "image": {
                      "imageUrl": "https://cataas.com/cat"
                     }
                  }
                ]
              }
            ]
          }
        }
      ]
    }
  };
}