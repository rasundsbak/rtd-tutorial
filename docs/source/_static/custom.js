exports.createPages = async function ({ actions, graphql }) {
    const { data } = await graphql(` /* some graphQL query */ `);
    data.allMarkdownRemark.edges.forEach((edge) => {
        const alternativeHtml = generateAlternativeHtml(edge.node.html);
        actions.createPage({
            component: require.resolve(`./src/templates/PostTemplate.jsx`),
            context: { alternativeHtml },
        })
    })
}

function generateAlternativeHtml(html) {
    const dom = new JSDOM(html);
    const { document } = dom.window;
    const codeSnippets = document.querySelectorAll('.gatsby-highlight');

    codeSnippets.forEach((codeSnippet) => {
        const wrapper = document.createElement('div');
        wrapper.classList.add('copy-code-block');

        // add your own css styles here, css classes, etc.
        const copyButton = document.createElement('button');
        copyButton.innerHTML = 'Copy';
        codeSnippet.insertAdjacentHTML(`afterend`, copyButton);
    });

    return document.body.innerHTML;
}

import copy from 'clipboard-copy';

const BlogPostTemplate = ({ data, pageContext }) => {
    const { alternativeHtml } = pageContext;

    useEffect(() => {
        const codeSnippets = document.querySelectorAll('.copy-code-block button');
        codeSnippets.forEach((elementWrapper) => {
            codeSnippet.addEventListener('click', () => {
                const codeSnippet = elementWrapper.parentElement.querySelector('.gatsby-highlight');
                const code = codeSnippet.innerHTML;
                copy(code);
            });
        });
    }, []);

    return (
        <section>
            <h1>{data.markdownRemark.frontmatter.title}</h1>
            <div dangerouslySetInnerHTML={{ __html: alternativeHtml }} />
        </section>
    );
};
