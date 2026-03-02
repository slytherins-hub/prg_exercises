(function () {
    var LEADING_MARKERS_RE = /^[\s\u200B]*(?:📝|🌟|💡|⚠️|📘)\s*/u;

    function getLeadingStrong(element) {
        if (!element || element.tagName !== 'P') {
            return null;
        }

        return element.querySelector(':scope > strong:first-child');
    }

    function normalizeLabelText(text) {
        return (text || '')
            .replace(LEADING_MARKERS_RE, '')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function classifyLabel(text) {
        var normalized = normalizeLabelText(text).toLowerCase();

        if (/^úkol\b/.test(normalized)) {
            return 'task';
        }

        if (/^bonus/.test(normalized)) {
            return 'bonus';
        }

        if (/^(tip|poznámka|nápověda)\b/.test(normalized)) {
            return 'tip';
        }

        return null;
    }

    function applyFormatClass(element, type) {
        if (!element || !type) {
            return;
        }

        element.classList.add('fmt-label', 'fmt-' + type);
    }

    function enhanceFormatMarkers() {
        var container = document.querySelector('.md-content__inner');
        if (!container) {
            return;
        }

        var headings = container.querySelectorAll('h2, h3, h4');
        headings.forEach(function (heading) {
            var markerType = classifyLabel(heading.textContent || '');
            applyFormatClass(heading, markerType);
        });

        var strongLabels = container.querySelectorAll('p > strong:first-child, blockquote > p > strong:first-child');
        strongLabels.forEach(function (strong) {
            var markerType = classifyLabel(strong.textContent || '');
            applyFormatClass(strong, markerType);
        });
    }

    function getHeadingLevel(element) {
        if (!element || !element.tagName || !/^H[1-6]$/.test(element.tagName)) {
            return 7;
        }

        return Number(element.tagName.slice(1));
    }

    function isBonusSectionHeading(element) {
        if (!element || element.tagName !== 'H2') {
            return false;
        }

        var normalized = normalizeLabelText(element.textContent || '').toLowerCase();
        return /^bonus/.test(normalized);
    }

    function isExplicitTaskOrBonusStart(element) {
        if (!element || !element.tagName) {
            return false;
        }

        if (/^H[2-4]$/.test(element.tagName)) {
            if (element.classList.contains('fmt-task')) {
                return true;
            }

            if (/^H[3-4]$/.test(element.tagName) && element.classList.contains('fmt-bonus')) {
                return true;
            }
        }

        if (element.tagName === 'P') {
            var strong = getLeadingStrong(element);
            return !!(strong && (strong.classList.contains('fmt-task') || strong.classList.contains('fmt-bonus')));
        }

        return false;
    }

    function isTaskStart(element) {
        return isExplicitTaskOrBonusStart(element);
    }

    function findTaskStarts(container) {
        var starts = [];
        var children = Array.from(container.children);
        var inBonusSection = false;

        children.forEach(function (child) {
            if (/^H[1-6]$/.test(child.tagName)) {
                if (child.tagName === 'H2') {
                    inBonusSection = isBonusSectionHeading(child);
                } else if (getHeadingLevel(child) <= 2) {
                    inBonusSection = false;
                }
            }

            if (isTaskStart(child)) {
                starts.push(child);
                return;
            }

            if (inBonusSection && /^H[3-4]$/.test(child.tagName)) {
                starts.push(child);
            }
        });

        return starts;
    }

    function enhanceTaskBlocks() {
        var container = document.querySelector('.md-content__inner');
        if (!container) {
            return;
        }

        var taskStarts = findTaskStarts(container);

        taskStarts.forEach(function (startNode) {
            if (!startNode || startNode.parentElement !== container || startNode.closest('.fmt-task-block')) {
                return;
            }

            var wrapper = document.createElement('div');
            wrapper.className = 'fmt-task-block';
            container.insertBefore(wrapper, startNode);

            var isHeadingTask = /^H[2-4]$/.test(startNode.tagName);
            var startLevel = getHeadingLevel(startNode);
            var current = startNode;

            while (current) {
                var next = current.nextElementSibling;
                wrapper.appendChild(current);

                if (!next) {
                    break;
                }

                if (next.tagName === 'HR') {
                    break;
                }

                if (isTaskStart(next)) {
                    break;
                }

                if (/^H[1-6]$/.test(next.tagName)) {
                    if (!isHeadingTask || getHeadingLevel(next) <= startLevel) {
                        break;
                    }
                }

                current = next;
            }
        });
    }

    function isQuestionParagraph(element) {
        if (!element || element.tagName !== 'P') {
            return false;
        }

        var strong = element.querySelector(':scope > strong:only-child');
        if (!strong) {
            return false;
        }

        return /^\d+\.\s+/.test(strong.textContent.trim());
    }

    function getQuestionText(paragraph) {
        var strong = paragraph.querySelector(':scope > strong:only-child');
        if (!strong) {
            return '';
        }

        return strong.textContent.trim().replace(/^\d+\.\s+/, '');
    }

    function enhanceSelfCheck() {
        var path = window.location.pathname.toLowerCase();
        var pageLooksLikeSelfCheck = path.indexOf('self_check') !== -1 || path.indexOf('self-check') !== -1;

        if (!pageLooksLikeSelfCheck) {
            return;
        }

        document.body.classList.add('page-selfcheck');

        var container = document.querySelector('.md-content__inner');
        if (!container) {
            return;
        }

        var children = Array.from(container.children);
        var currentList = null;

        for (var index = 0; index < children.length; index += 1) {
            var node = children[index];

            if (!isQuestionParagraph(node)) {
                currentList = null;
                continue;
            }

            if (!currentList) {
                currentList = document.createElement('ol');
                currentList.className = 'quiz-questions';
                container.insertBefore(currentList, node);
            }

            var listItem = document.createElement('li');
            var questionParagraph = document.createElement('p');
            questionParagraph.className = 'quiz-question';
            questionParagraph.textContent = getQuestionText(node);
            listItem.appendChild(questionParagraph);
            currentList.appendChild(listItem);

            var sibling = node.nextElementSibling;
            while (sibling) {
                var nextSibling = sibling.nextElementSibling;
                var tag = sibling.tagName;

                if (isQuestionParagraph(sibling)) {
                    break;
                }

                if (tag === 'H1' || tag === 'H2' || tag === 'H3') {
                    break;
                }

                listItem.appendChild(sibling);
                sibling = nextSibling;
            }

            node.remove();
        }
    }

    function runEnhancements() {
        enhanceFormatMarkers();
        enhanceTaskBlocks();
        enhanceSelfCheck();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runEnhancements);
    } else {
        runEnhancements();
    }
})();
