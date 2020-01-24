const axios = require('axios');
const sanitizeHtml = require('sanitize-html');

exports.handler = async (event) => {

    const { GITHUB_API_KEY } = process.env;
    const REPO = 'himmelseng';
    const USER = 'sverrejb';
    const PUBLISH_BRANCH = 'v3';
    const MODERATION = true;
    const github_api_url = 'https://api.github.com'
    const github_headers = {
        'User-Agent': USER,
        'Content-Type': 'application/json',
        'Authorization': `token ${GITHUB_API_KEY}`
    }

    console.log(event)

    let SUBMIT_EVENT_BODY;
    if (process.env.AWS_LAMBDA_FUNCTION_VERSION) {
        SUBMIT_EVENT_BODY = JSON.parse(event.body)
    }
    else {
        SUBMIT_EVENT_BODY = {
            name: "Test",
            comment: "Lorem Ipsum"
        }
    }

    const ref_uri = `${github_api_url}/repos/${USER}/${REPO}/git/refs/heads/${PUBLISH_BRANCH}`
    const ref_response = await axios.get(ref_uri, { 'headers': github_headers })
        .catch((err) => {
            console.log(err.message)
        });

    const master_branch_SHA = ref_response.data.object.sha;
    const branch_name = `${Date.now()}_${SUBMIT_EVENT_BODY.name}`
    const branch_url = `${github_api_url}/repos/${USER}/${REPO}/git/refs`
    const branch_data = {
        ref: `refs/heads/${branch_name}`,
        sha: master_branch_SHA
    };
    if (MODERATION) {

        await axios({
            method: 'post',
            url: branch_url,
            data: branch_data,
            headers: github_headers
        }).catch((err) => {
            console.log(err.message)
        });
    }

    const dirty_data = JSON.stringify(SUBMIT_EVENT_BODY);
    const clean_data = sanitizeHtml(dirty_data, {
        allowedTags: [],
        allowedAttributes: {},
      });
    const buff = new Buffer(clean_data);
    const file_data = buff.toString('base64');
    const file_name = `verse_${branch_name}`;
    const commit_url = `${github_api_url}/repos/${USER}/${REPO}/contents/verses/${file_name}.txt`

    const commit_data = {
        message: "Added new verse",
        committer: {
            name: "Monalisa Octocat",
            email: "octocat@github.com"
        },
        branch: MODERATION ? branch_name : PUBLISH_BRANCH,
        content: file_data
    }

    await axios({
        method: 'put',
        url: commit_url,
        data: commit_data,
        headers: github_headers
    }).catch((err) => {
        console.log(err.message)
    });

    const pullrequest_url = `${github_api_url}/repos/${USER}/${REPO}/pulls`
    const pullrequest_data = {
        title: `New verse added: ${SUBMIT_EVENT_BODY.name}`,
        body: SUBMIT_EVENT_BODY.comment,
        head: branch_name,
        base: PUBLISH_BRANCH,
        maintainer_can_modify: true
    };

    await axios({
        method: 'post',
        url: pullrequest_url,
        data: pullrequest_data,
        headers: github_headers
    }).catch((err) => {
        console.log(err.message)
    });

    return {
        statusCode: 200,
        body: "ok",
    }
};